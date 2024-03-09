from unittest import TestCase
from chain.chains import ThesisSummaryChain

import logging

logging.basicConfig(level=logging.WARNING)


class ChainTest(TestCase):
    def setUp(self) -> None:
        self.chain = ThesisSummaryChain()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_invoke(self) -> None:
        url = "https://arxiv.org/pdf/1706.03762.pdf"

        template_variable_table: dict = {"subject": "AI thesis"}
        # map prompt template
        map_document_variable = "pages"
        map_system_prompt_template = "You are the best AI thesis summary assistant about pages. This is partial of documents. Please summary about this page well."
        map_partial_document_prompt_template = "{pages}"

        # reduce prompt template
        reduce_document_variable = "doc_summaries"
        reduce_system_prompt_template = "You are the best AI thesis summary assistant about documents. This is set of thesis summary. Please summary about this set well."
        reduce_partial_document_prompt_template = "{doc_summaries}"

        from langchain_core.documents.base import Document

        documents = [
            Document(
                page_content="""What is MLOps?
Machine learning operations (MLOps) are a set of practices that automate and simplify machine learning (ML) workflows and deployments. Machine learning and artificial intelligence (AI) are core capabilities that you can implement to solve complex real-world problems and deliver value to your customers. MLOps is an ML culture and practice that unifies ML application development (Dev) with ML system deployment and operations (Ops). Your organization can use MLOps to automate and standardize processes across the ML lifecycle. These processes include model development, testing, integration, release, and infrastructure management."""
            ),
            Document(
                page_content="""Why is MLOps required? At a high level, to begin the machine learning lifecycle, your organization typically has to start with data preparation. You fetch data of different types from various sources, and perform activities like aggregation, duplicate cleaning, and feature engineering.

After that, you use the data to train and validate the ML model. You can then deploy the trained and validated model as a prediction service that other applications can access through APIs.

Exploratory data analysis often requires you to experiment with different models until the best model version is ready for deployment. It leads to frequent model version deployments and data versioning. Experiment tracking and ML training pipeline management are essential before your applications can integrate or consume the model in their code.

MLOps is critical to systematically and simultaneously manage the release of new ML models with application code and data changes. An optimal MLOps implementation treats the ML assets similarly to other continuous integration and delivery (CI/CD) environment software assets. You deploy ML models alongside the applications and services they use and those that consume them as part of a unified release process."""
            ),
            Document(
                page_content="""What are the principles of MLOps?
Next, we explain four key principles of MLOps.

Version control
This process involves tracking changes in the machine learning assets so you can reproduce results and roll back to previous versions if necessary. Every ML training code or model specification goes through a code review phase. Each is versioned to make the training of ML models reproducible and auditable.

Reproducibility in an ML workflow is important at every phase, from data processing to ML model deployment. It means that each phase should produce identical results given the same input.

Automation
Automate various stages in the machine learning pipeline to ensure repeatability, consistency, and scalability. This includes stages from data ingestion, preprocessing, model training, and validation to deployment.

These are some factors that can trigger automated model training and deployment:

Messaging
Monitoring or calendar events
Data changes
Model training code changes
Application code changes.
Automated testing helps you discover problems early for fast error fixes and learnings. Automation is more efficient with infrastructure as code (IaC). You can use tools to define and manage infrastructure. This helps ensure it's reproducible and can be consistently deployed across various environments"""
            ),
            Document(
                page_content="""What are the benefits of MLOps?
Machine learning helps organizations analyze data and derive insights for decision-making. However, it's an innovative and experimental field that comes with its own set of challenges. Sensitive data protection, small budgets, skills shortages, and continuously evolving technology limit a project's success. Without control and guidance, costs may spiral, and data science teams may not achieve their desired outcomes.

MLOps provides a map to guide ML projects toward success, no matter the constraints. Here are some key benefits of MLOps.

Faster time to market
MLOps provides your organization with a framework to achieve your data science goals more quickly and efficiently. Your developers and managers can become more strategic and agile in model management. ML engineers can provision infrastructure through declarative configuration files to get projects started more smoothly.

Automating model creation and deployment results in faster go-to-market times with lower operational costs. Data scientists can rapidly explore an organization's data to deliver more business value to all.

Improved productivity
MLOps practices boost productivity and accelerate the development of ML models. For instance, you can standardize the development or experiment environment. Then, your ML engineers can launch new projects, rotate between projects, and reuse ML models across applications. They can create repeatable processes for rapid experimentation and model training. Software engineering teams can collaborate and coordinate through the ML software development lifecycle for greater efficiency.

Efficient model deployment
MLOps improves troubleshooting and model management in production. For instance, software engineers can monitor model performance and reproduce behavior for troubleshooting. They can track and centrally manage model versions and pick and choose the right one for different business use cases.

When you integrate model workflows with continuous integration and continuous delivery (CI/CD) pipelines, you limit performance degradation and maintain quality for your model. This is true even after upgrades and model tuning."""
            ),
        ]
        result = self.chain.invoke(
            map_document_variable=map_document_variable,
            map_system_prompt_template=map_system_prompt_template,
            map_user_prompt_template=map_partial_document_prompt_template,
            reduce_system_prompt_template=reduce_system_prompt_template,
            reduce_user_prompt_template=reduce_partial_document_prompt_template,
            reduce_document_variable=reduce_document_variable,
            documents=documents,
            template_variable_table=template_variable_table,
            file_uri=url,
        )

        self.assertIsInstance(result, str)
