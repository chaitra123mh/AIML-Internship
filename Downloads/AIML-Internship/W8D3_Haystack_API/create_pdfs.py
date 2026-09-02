from reportlab.pdfgen import canvas

documents = {
    "ai.pdf": "Artificial Intelligence is the field of creating computer systems that can perform tasks that normally require human intelligence.",
    "machine_learning.pdf": "Machine Learning is a branch of Artificial Intelligence that allows computers to learn patterns from data and make predictions.",
    "deep_learning.pdf": "Deep Learning is a type of Machine Learning that uses neural networks with multiple layers to learn complex patterns.",
    "nlp.pdf": "Natural Language Processing is a field of Artificial Intelligence that helps computers understand and process human language.",
    "computer_vision.pdf": "Computer Vision is a field of Artificial Intelligence that enables computers to understand and analyze images and videos."
}

for filename, text in documents.items():
    pdf = canvas.Canvas(filename)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 750, text)
    pdf.save()

print("5 PDF files created successfully!")