from excuse.models import Excuse

Excuse.objects.create(content="It was working in my head")
Excuse.objects.create(content="I thought I fixed that")
Excuse.objects.create(content="Actually, that is a feature")

Excuse.objects.all()
for excuse in Excuse.objects.all():
    print excuse.content
