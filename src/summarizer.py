from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import logging
from typing import Optional

class Summarizer:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.llm_o1 = ChatOpenAI(model="o1-preview", temperature=1)
        self.llm_4o = ChatOpenAI(model="gpt-4o", temperature=0.1)
        self.summary_chain = self._create_summary_chain()
        self.qa_chain = self._create_qa_chain()
        self.final_chain = self._create_final_chain()

    def summarize(self, transcript: str) -> str:
        """Summarize transcript using advanced summary chain"""
        try:
            final_report = self.final_chain.invoke({"transcript": transcript})
            return final_report
        except Exception as e:
            logging.error(f"Error in summarization: {str(e)}")
            raise

    def _create_summary_chain(self):
        summary_prompt = """
        请帮我处理以下的逐字稿，从相关行业投资者的角度考虑一下有什么值得参考的信息和趋势，进行总结和分析，要求如下:

        1. 请用中文进行报告总结
        2. 考虑到一些术语观众可能不熟悉，请在技术术语后面附上英文原文。
        3. 在报告末尾加上报告中出现术语的简要解释。
        逐字稿: 
        {transcript}
        """
        summary_prompt = PromptTemplate.from_template(summary_prompt)
        return summary_prompt | self.llm_o1 | StrOutputParser()

    def _create_qa_chain(self):
        qa_prompt = """
        请从投资者的角度考虑本文中涉及了哪些问题与重要信息。并以问答的形式添加在报告的开头，并给出分析的同时引用原文，引用原文是请保持原文的语言。
        格式请参考如下的例子:
        **问1**：Elastic在2025财年第二季度的关键财务亮点是什么？

        **答**：Elastic在2025财年第二季度取得了强劲的财务业绩，超出了所有收入和盈利指标的指引。总收入达到3.65亿美元，同比增长18%，云收入同比增长25%。公司还实现了17.6%的非GAAP运营利润率，显著高于预期。

        **引用原文**：

        > "Elastic delivered a strong second quarter, supported by solid sales execution and customer commitments. In Q2, we meaningfully exceeded guidance across all revenue and profitability metrics. Revenue grew by 18% year-over-year. Cloud revenue grew by 25% year-over-year. And we delivered a non-GAAP operating margin of 18%."
        > 

        Transcript:
        {transcript}
        """
        qa_prompt = PromptTemplate.from_template(qa_prompt)
        return qa_prompt | self.llm_o1 | StrOutputParser()

    def _create_final_chain(self):
        final_prompt = """
        你将会得到关于同一份逐字稿的两份报告，一份是问答形式的，另一份是总结形式的。
        请将两份报告合并成一份，问答报告放在总结报告的前面。
        请不要修改问答报告和总结报告的内容，只需将两份报告合并。
        请以：标题 - 摘要 - Q&A部分 - 总结报告 的形式返回。

        问答报告:
        {QA}
        总结报告:
        {Summary}
        """
        final_prompt = PromptTemplate.from_template(final_prompt)
        mapping = {"QA": self.qa_chain, "Summary": self.summary_chain}
        return mapping | final_prompt | self.llm_4o | StrOutputParser()