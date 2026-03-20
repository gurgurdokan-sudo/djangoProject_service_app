from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import User, ServiceMaster, ServicePlan
from .excel.service_sheet import create_service_sheet
from .forms import UserForm
#利用者一覧
def user_list(request):
    users = User.objects.all()
    return render(request, 'dashboard/user_list.html', {'users': users})
#新規作成
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'新規登録完了しました')
            return redirect('dashboard:user_list')
    else:
        form = UserForm()
    return render(request,'dashboard/user_form.html', {'form': form})
#Excel出力
def export_service_sheet(request, user_id, year, month):
    user = User.objects.get(id=user_id)
    wb = create_service_sheet(user, year, month)

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="【様式】サービス提供票・別表"'

    wb.save(response)
    return response
#更新
def user_update(request, user_id):
    user = get_object_or_404(User,id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,f'{user.name}さんを更新されました')
            return redirect('dashboard:user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'dashboard/user_form.html', {'form': form})
#詳細
def user_detail(request,user_id):
    target = get_object_or_404(User,id=user_id)
    labels = {f.name: f.verbose_name for f in target._meta.fields}
    return render(request,'dashboard/user_detail.html',{'user': target,'labels': labels,})
#消去
def user_delete(request,user_id):
    target = get_object_or_404(User,id=user_id)
    if request.method=='POST':
        target.delete()
        messages.error(request,f'{user.name}さんを消去しました')
        return redirect('dashboard:user_list')
    return render(request,'dashboard/user_delete.html',{'user':target})
#サービス提供票
def user_service(request,user_id):
    target = get_object_or_404(User,id=user_id)
    plan = ServicePlan.objects.get(user=target)
    service = ServiceMaster.objects.all()
    print(plan.stay_time_category)
    naiyou = ServiceMaster.get_quer_plan(level=target.care_level,stay_time_category = '5-6').first()
    context = {
        'user': target,
        'plan': plan,
        'service': service,
        'naiyou':naiyou,
    }
    return render(request,'dashboard/user_service.html',{'context':context})