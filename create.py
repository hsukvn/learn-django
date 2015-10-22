from excuse.models import Excuse

def main():
    Excuse.objects.all().delete()
    Excuse.objects.create(content="It was working in my head")
    Excuse.objects.create(content="I thought I fixed that")
    Excuse.objects.create(content="Actually, that is a feature")

    for excuse in Excuse.objects.all():
        print excuse.content
