from asyncflows import Action, BaseModel, Field
from asyncflows.log_config import get_logger
import os

log = get_logger()

api_base= os.getenv('api_base')

class Inputs(BaseModel):
    role: str = Field(
        description="The Job title the candidate is interested in"
    )
    resume_text: str = Field(
        description="The resume of the candidate"
    )
    job_description: str = Field(
        description="The description of the job the candidate is interested in"
    )
    name: str = Field(
        description="The Name of the candidate applying for the job"
    )
    hiring_manager: str = Field(
        description="The hiring manager of the company"
    )
    referral: str = Field(
        description="Where the candidate learned about the job vacancy"
    )
    company: str = Field(
        description="The Company which the candidate wants to work in"
    )
    cand_address: str = Field(
        description="The address of the candidate"
    )
    comp_address: str = Field(
        description="The address of the company"
    )
    

class Outputs(BaseModel):
    cover_letter: str = Field(
        description="The generated cover letter"
    )

class GenerateCoverLetter(Action[Inputs, Outputs]):
    name = 'generate_cover_letter'
    
    async def run(self, inputs: Inputs) -> Outputs:
        cover_letter_template = f"""
        [name]
        [Your Address]
        [City, State, ZIP Code]
        [Today’s Date]

        [Hiring Manager’s Name]
        [Company Name]
        [Company Address]
        [City, State, ZIP Code]

        Dear [Hiring Manager’s Name],

        I am writing to express my interest in the [Role] position at [Company Name]. With my background in [Relevant Skills or Experience], I am excited about the opportunity to contribute to your team. I learned about this job opening through [Referral].

        As detailed in my resume, I have [X years] of experience in [Field or Industry], with a strong focus on [Relevant Skills or Experience]. I am particularly drawn to this role because [Reason for Interest].

        Thank you for considering my application. I look forward to the possibility of discussing this exciting opportunity with you. Please feel free to contact me at [Your Phone Number] or [Your Email Address].

        Sincerely,
        [name]
        """

        # Replace placeholders with actual input values
        cover_letter = cover_letter_template.format(
            role=inputs.role,
            name=inputs.name,
            hiring_manager=inputs.hiring_manager,
            company=inputs.company,
            cand_address=inputs.cand_address,
            comp_address=inputs.comp_address,
            referral=inputs.referral,
            resume_text=inputs.resume_text,
            job_description=inputs.job_description
        )
        
        return Outputs(cover_letter=cover_letter.strip())
