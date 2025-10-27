from pydantic import BaseModel, Field
class ExtractedData(BaseModel):
    """Data extracted from a LinkedIn post."""
    job_title: str = Field(description="The professional title being advertised for, e.g., 'Freelance WordPress Developer'.")
    post_url: str = Field(description="The URL of the LinkedIn post.")
    hiring_task: str = Field(description="The task which has to been done inorder to apply for the job. eg- Submit the resume in DM")
class AllExtractedData(BaseModel):
    """A list of all extracted data."""
    extracted_data: list[ExtractedData]
