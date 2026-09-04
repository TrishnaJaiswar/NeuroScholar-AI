from typing import TypedDict, Optional
from pydantic import BaseModel , Field
from typing import List, Literal , Dict , Any

class PlannerOutput(BaseModel):
    # What the user wants to do
    task: Literal[
        "qa",
        "compare_papers",
        "literature_review",
        "trend_analysis",
        "summarize",
        "report_generation"
    ] = Field(description="Primary research task")

    # Which agents LangGraph should execute
    agents: List[
        Literal[
            "retrieval",
            "research",
            "analysis",
            "critic",
            "citation",
            "report"
        ]
    ] = Field(description="Ordered execution plan")

    # Whether RAG retrieval is required
    use_rag: bool = Field(description="Use Advanced RAG or not")

    # Number of documents to retrieve
    top_k: int = Field(default=8, ge=1, le=20)

    # Whether hybrid retrieval should be enabled
    retrieval_mode: Literal["dense", "hybrid"] = "hybrid"

    # Whether metadata filtering is needed
    use_metadata_filter: bool = False

    # User-facing reasoning (for debugging/observability)
    reasoning: str = Field(description="Why this workflow was selected")
    

class RetrievedChunk(BaseModel):
    document_id: str
    source: str
    page: int
    content: str
    score: float
    metadata: Dict[str, Any]



class ResearchInsight(BaseModel):
    topic: str
    finding: str
    evidence: str

class ResearchOutput(BaseModel):
    summary: str
    insights: List[ResearchInsight]



class RetrievalOutput(BaseModel):
    query: str
    chunks: List[RetrievedChunk]


class ComparisonItem(BaseModel):
    criterion: str
    paper_a: str
    paper_b: str

class TrendItem(BaseModel):
    trend: str
    description: str

class AnalysisOutput(BaseModel):
    comparisons: List[ComparisonItem]
    trends: List[TrendItem]
    conclusion: str


class VerificationIssue(BaseModel):
    claim: str
    supported: bool
    reason: str

class CriticOutput(BaseModel):
    verified: bool
    confidence: float
    issues: List[VerificationIssue]

class Citation(BaseModel):
    source: str
    page: int
    quote: str

class CitationOutput(BaseModel):
    citations: List[Citation]

class ReportSection(BaseModel):
    heading: str
    content: str


class ReportOutput(BaseModel):
    title: str
    abstract: str
    introduction: str
    key_findings: List[str]
    comparative_analysis: str
    limitations: str
    conclusion: str
    references: List[str]


class ResearchState(TypedDict):
    question: str

    # Frontend
    forced_task: Optional[str]
    selected_documents: List[str]

    # Workflow
    planner: Optional[PlannerOutput]
    retrieval: Optional[RetrievalOutput]
    research: Optional[ResearchOutput]
    analysis: Optional[AnalysisOutput]
    critic: Optional[CriticOutput]
    citation: Optional[CitationOutput]
    report: Optional[ReportOutput]

    # Final response
    answer: str