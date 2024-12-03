# summarizer.py

from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import logging
from typing import Optional
from src.prompts import PROMPTS

class Summarizer:
    def __init__(self):
        self.client = OpenAI()
        self.llm_o1 = ChatOpenAI(model="o1-preview", temperature=1)
        self.llm_4o = ChatOpenAI(model="gpt-4o", temperature=0.1)

    def summarize(
        self,
        transcript: str,
        chain_type: str = "final",
        summary_prompt_key: Optional[str] = None,
        qa_prompt_key: Optional[str] = None,
        final_prompt_key: Optional[str] = None
    ) -> str:
        """Summarize transcript using specified chain."""
        try:
            if chain_type == "summary":
                chain = self._create_summary_chain(summary_prompt_key)
                return chain.invoke({"transcript": transcript})
            elif chain_type == "qa":
                chain = self._create_qa_chain(qa_prompt_key)
                return chain.invoke({"transcript": transcript})
            elif chain_type == "final":
                chain = self._create_final_chain(summary_prompt_key, qa_prompt_key, final_prompt_key)
                return chain.invoke({"transcript": transcript})
            else:
                raise ValueError(f"Invalid chain_type: {chain_type}")
        except Exception as e:
            logging.error(f"Error in summarization: {str(e)}")
            raise

    def _get_prompt(self, prompt_key: Optional[str], default_prompt_key: str) -> str:
        if prompt_key and prompt_key in PROMPTS:
            return PROMPTS[prompt_key]
        else:
            return PROMPTS[default_prompt_key]

    def _create_summary_chain(self, summary_prompt_key: Optional[str] = None):
        summary_prompt = self._get_prompt(summary_prompt_key, 'default_summary_prompt')
        summary_prompt = PromptTemplate.from_template(summary_prompt)
        return summary_prompt | self.llm_o1 | StrOutputParser()

    def _create_qa_chain(self, qa_prompt_key: Optional[str] = None):

        qa_prompt = self._get_prompt(qa_prompt_key, 'default_qa_prompt')
        qa_prompt = PromptTemplate.from_template(qa_prompt)
        return qa_prompt | self.llm_o1 | StrOutputParser()

    def _create_final_chain(
        self,
        summary_prompt_key: Optional[str] = None,
        qa_prompt_key: Optional[str] = None,
        final_prompt_key: Optional[str] = None
    ):
    
        final_prompt = self._get_prompt(final_prompt_key, 'default_final_prompt')
        final_prompt = PromptTemplate.from_template(final_prompt)
        qa_chain = self._create_qa_chain(qa_prompt_key)
        summary_chain = self._create_summary_chain(summary_prompt_key)
        mapping = {"QA": qa_chain, "Summary": summary_chain}
        return mapping | final_prompt | self.llm_o1 | StrOutputParser()