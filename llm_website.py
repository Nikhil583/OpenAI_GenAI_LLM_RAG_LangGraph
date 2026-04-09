import os
import warnings
from dotenv import load_dotenv

from openai import OpenAI
from anthropic import Anthropic
import google.generativeai as genai

load_dotenv()

#Client Initialization
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
claude_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

#GenAI Model Initialization
gemini_model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# #Prompt
# test_message = "What is the capital of France and its history?"

# #Response from all three models
# response_openai = openai_client.chat.completions.create(
#     model="gpt-4o-mini",
#     message = [{"role": "user", "content": test_message}]
# )
# response_google = gemini_model.generate_content(test_message)
# response_anthropic = claude_client.chat.completions.create(
#     model="claude-3-5-sonnet-20241022",
#     max_tokens=1024,
#     messages=[{"role": "user", "content": test_message}]
# )

print("OpenAI Response:", response_openai.choices[0].message.content)
print("Google GenAI Response:", response_google.text)
print("Anthropic Response:", response_anthropic.choices[0].message.content)

prompt_message = """
# Professional Portfolio Website - Development Prompt

## Project Overview
Create a single-page, responsive portfolio website in `index.html` with internal CSS that showcases professional information and enables recruiter contact.

## Required Sections
1. **Header/Navigation** - Professional branding and navigation menu
2. **About/Summary** - Professional journey and career summary
3. **Skills Section** - Technical and professional competencies
4. **Experience Timeline** - Years of experience and work history
5. **Education** - Degrees, certifications, and qualifications
6. **Contact Form** - Lead generation form for recruiter outreach (interview requests, inquiries)
7. **Footer** - Copyright and social media links

## Technical Requirements
- **Single File**: All HTML and CSS in one `index.html` file
- **Responsive Design**: Mobile-first approach, works on all devices (mobile, tablet, desktop)
- **Internal CSS**: Style rules embedded in `<style>` tag within HTML
- **No External Dependencies**: Self-contained, no external frameworks required
- **Form Functionality**: Contact form should be functional (use `mailto:` for demonstration)
- **Proper spacing and layout**: Clear sections with appropriate spacing and alignment
- **Form Functionality**: Form structure ready for backend integration
- **Professional Aesthetic**: Clean, modern design with a professional tone
- **Name and Branding**: Prominent display of name and professional branding in header
- **Color Scheme**: Professional colors (e.g., blues, grays, whites)
- **Background color**: dark background color with light text for a modern look
- **Typography**: Clear, professional fonts (e.g., sans-serif)
- **Navigation**: Smooth scrolling to sections, fixed header for easy access and hide the navigation bar into three lines on mobile view
- **Hover Effects**: Subtle hover effects for interactivity (optional)
- **form div styling**: Clear labels, input fields, and submit button with appropriate spacing and alignment and should be divided into two columns on desktop view and one column on mobile view with some cool background color and image on the other side of the form

## Design Considerations
- Clean, professional layout
- Clear typography and spacing
- Accessible color scheme
- Smooth navigation flow
- Professional visual hierarchy
- Subtle animations or interactions (optional)
- SEO-friendly structure (use of semantic HTML tags)
"""

#Response from all three models
response_openai = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    message = [{"role": "user", "content": prompt_message}]
)
response_google = gemini_model.generate_content(prompt_message)
response_anthropic = claude_client.chat.completions.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{"role": "user", "content": prompt_message}]
)