from reportlab.pdfgen import canvas

pdf = canvas.Canvas("sample.pdf")
pdf.drawString(100, 750, "W6D5 Document Chatbot")
pdf.drawString(100, 720, "LangChain and Ollama can be used to build document chatbots.")
pdf.drawString(100, 690, "A document chatbot retrieves information and uses an LLM to answer questions.")
pdf.save()

print("sample.pdf created successfully")