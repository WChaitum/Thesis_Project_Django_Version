from django.shortcuts import render,redirect
from ThesisApp.models import Person
from django.contrib import messages

# Create your views here.

# การแสดงข้อมูล
def index(request):
    all_person = Person.objects.filter(status="Call").first()
    if request.method == 'POST':
        search_keyword = request.POST.get('search_keyword', '')
        person = Person.objects.filter(Parent_key=search_keyword).first()
        if person:
            person.status = 'Call'
            person.save()
            messages.success(request, f'ได้รับข้อมูลของ คุณ{person.Parent_name} เรียบร้อยแล้ว')
            return redirect('/')
        else:
            messages.error(request, 'ไม่พบข้อมูลบุคคลนี้ในระบบ')
        # return redirect('/')
    return render(request, 'index.html', {'all_person': all_person})


def update_status(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.status = "Called"
        person.save()
    return redirect('/')

def member(request):
    all_person = Person.objects.all()
    return render(request,"member.html",{"all_person":all_person})



def about(request):
    return render(request,"about.html")

# การเพิ่มข้อมูล
def form(request):
    if request.method == "POST":
        # รับข้อมูล
        Parent_Name = request.POST.get("Parent_Name")
        Children_Name = request.POST.get("Children_Name")
        Parent_Key = request.POST.get("Parent_Key")

        if Parent_Name and Children_Name and Parent_Key:
            print("Parent Name: " + Parent_Name, "Children Name: " + Children_Name)
            # บันทึกข้อมูล
            person = Person.objects.create(
                Parent_name=Parent_Name,
                Parent_key=Parent_Key,
                children_name=Children_Name,
                status = "New"
                
            )
            messages.success(request, "บันทึกข้อมูลเรียบร้อย")
            return redirect('/member')
        else:
            error_message = "กรุณากรอกข้อมูลให้ครบถ้วน"
            messages.error(request, error_message)
            print(error_message)
            return render(request, "form.html")
    else:
        return render(request, "form.html")


# การแก้ไขข้อมูล
def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.Parent_name = request.POST["Parent_Name"]
        person.children_name = request.POST["Children_Name"]
        person.Parent_key = request.POST["Parent_Key"]
        person.save()
        messages.success(request,"อัพเดทข้อมูลเรียบร้อย")
        return redirect('/member')
    else:
        # ดึงข้อมูลที่ต้องการแก้ไข
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})
    

# การลบข้อมูล  
def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect('/member')
