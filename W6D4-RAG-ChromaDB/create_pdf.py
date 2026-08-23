from reportlab.pdfgen import canvas

pdf = canvas.Canvas("sample.pdf")
pdf.drawString(100, 750, "W6D4 RAG Pipeline")
pdf.drawString(100, 720, "Retrieval Augmented Generation combines retrieval")
pdf.drawString(100, 690, "with language generation to answer questions.")
pdf.drawString(100, 660, "ChromaDB stores and retrieves relevant information.")
pdf.save()

print("sample.pdf created successfully")