# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from User.models import CustomUser
from Client.models import AccountType, Client, ClientAccountantInfo, ClientBankInfo, ClientLegalInfo, ClientPassword, Services, AccountType
from Client.forms import (AccountTypeForm,
                    ClientAccountantInfoForm,
                    ClientBankInfoForm,
                    ClientForm,
                    ClientLegalInfoForm,
                    ClientPasswordForm,
                    AccountTypeForm,)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
#@login_required(login_url='login')
def AddClientView(request):

    if request.method == 'POST':
        messages.add_message(request, messages.SUCCESS, 'Client is added')
        client_form = ClientForm(request.POST)
        clientBankInfo_Form = ClientBankInfoForm(request.POST)
        clientAccountantInfo_Form = ClientAccountantInfoForm(request.POST)
        clientLegalInfo_Form = ClientLegalInfoForm(request.POST)
        clientPassword_Form = ClientPasswordForm(request.POST)
        if ( client_form.is_valid()
             and clientAccountantInfo_Form.is_valid()
             and clientBankInfo_Form.is_valid()
             and clientLegalInfo_Form.is_valid()
             and clientPassword_Form.is_valid()):

             user = CustomUser.objects.create_user(
                   username = name,
                   first_name = firstname,
                   last_name = lastname,
                   password = firstname
             )
             client = client_form.save(commit=False)
             client.user = user
             client.save()
             form_list = []
             form_list.append(clientAccountantInfo_Form.save(commit=False))
             form_list.append(clientBankInfo_Form.save(commit=False))
             form_list.append(clientLegalInfo_Form.save(commit=False))
             form_list.append(clientPassword_Form.save(commit=False))

             for form in form_list:
                if form.client is None:
                     form.client = client
                form.save()
             client_form = ClientForm()
             clientBankInfo_Form = ClientBankInfoForm()
             clientAccountantInfo_Form = ClientAccountantInfoForm()
             clientLegalInfo_Form = ClientLegalInfoForm()
             clientPassword_Form = ClientPasswordForm()
             # Begin Mail..............
             subject = 'Work On Your Application has been started..'
             message = ' It Will be Completed soon '
             email_from = settings.EMAIL_HOST_USER
             recipient_list = ['',] #inwardform.inward_client_id.client_email
             send_mail( subject, message, email_from, recipient_list,fail_silently=False)
             # End Mail.................

    else:
        messages.add_message(request, messages.ERROR, 'Client is not added')
        client_form = ClientForm()
        clientBankInfo_Form = ClientBankInfoForm()
        clientAccountantInfo_Form = ClientAccountantInfoForm()
        clientLegalInfo_Form = ClientLegalInfoForm()
        clientPassword_Form = ClientPasswordForm()


    context = {
            'client_form': client_form,
            'clientBankInfo_Form': clientBankInfo_Form,
            'clientAccountantInfo_Form': clientAccountantInfo_Form,
            'clientLegalInfo_Form': clientLegalInfo_Form,
            'clientPassword_Form': clientPassword_Form,
        }
    return render(request, 'User/user.html', context)
    # return render(request, 'Client/add-client.html', context)

@login_required(login_url='login')
def UpdateClientView(request, id):

    client = get_object_or_404(Client, client_id=id)
    client_form = ClientForm(request.POST or None, instance=client)

    clientBankInfo = get_object_or_404(ClientBankInfo, client=id)
    clientBankInfo_Form = ClientBankInfoForm(request.POST or None, instance=clientBankInfo)

    clientAccountantInfo = get_object_or_404(ClientAccountantInfo, client=id)
    clientAccountantInfo_Form = ClientAccountantInfoForm(request.POST or None, instance=clientAccountantInfo)

    clientLegalInfo = get_object_or_404(ClientLegalInfo, client=id)
    clientLegalInfo_Form = ClientLegalInfoForm(request.POST or None, instance=clientLegalInfo)

    clientPassword = get_object_or_404(ClientPassword, client=id)
    clientPassword_Form = ClientPasswordForm(request.POST or None, instance=clientPassword)

    if ( client_form.is_valid()
          and clientAccountantInfo_Form.is_valid()
          and clientBankInfo_Form.is_valid()
          and clientLegalInfo_Form.is_valid()
          and clientPassword_Form.is_valid()):

          client = client_form.save()
          clientBankInfo_Form = clientBankInfo_Form.save()
          clientAccountantInfo_Form = clientAccountantInfo_Form.save()
          clientLegalInfo_Form = clientLegalInfo_Form.save()
          clientPassword_Form = clientPassword_Form.save()
          messages.add_message(request, messages.SUCCESS, 'Client is updated')
          return redirect('list-client')

    context = {
            'client_form': client_form,
            'clientBankInfo_Form': clientBankInfo_Form,
            'clientAccountantInfo_Form': clientAccountantInfo_Form,
            'clientLegalInfo_Form': clientLegalInfo_Form,
            'clientPassword_Form': clientPassword_Form,
        }

    return render(request, 'Client/add-client.html', context)

@login_required(login_url='login')
def DeleteClientView(request, id):
    obj = Client.objects.filter(client_id=id)
    name = str(obj[0])
    obj.delete()
    return render(request, 'delete_success.html', {'object':'Client', 'name':name})


# service views.............................................................................................

@login_required(login_url='login')
def AddServiceView(request):
    if request.method == 'POST':
        serviceForm = ServicesForm(request.POST or None)
        if serviceForm.is_valid():
            serviceForm.save()
        return redirect('added')
    else:
        serviceForm = ServicesForm(request.POST or None)
        return render(request, 'Client/add-service.html', {'form': serviceForm})

@login_required(login_url='login')
def UpdateServiceView(request, id):
    service = get_object_or_404(Services, pk=id)
    serviceForm = ServicesForm(request.POST or None, instance=service)
    if serviceForm.is_valid():
        serviceForm.save()
    return render(request, 'Client/add-service.html', {'form': serviceForm})

@login_required(login_url='login')
def DeleteServiceView(request, id):
    try:
        obj = Services.objects.get(service_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'Service', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})


# AccountType View ..................................................................................

@login_required(login_url='login')
def AddAccountTypeView(request):
    if request.method == 'POST':
        acountTypeForm = AccountTypeForm(request.POST or None)
        if acountTypeForm.is_valid():
            acountTypeForm.save()
        return redirect('added')
    else:
        acountTypeForm = AccountTypeForm(request.POST or None)
        return render(request, 'Client/add-service.html', {'form': acountTypeForm})

@login_required(login_url='login')
def UpdateAccountTypeView(request, id):
    service = get_object_or_404(AccountType, pk=id)
    acountTypeForm = AccountTypeForm(request.POST or None, instance=service)
    if acountTypeForm.is_valid():
        acountTypeForm.save()
    return render(request, 'Client/add-service.html', {'form': acountTypeForm})

@login_required(login_url='login')
def DeleteAccountTypeView(request, id):
    try:
        obj = AccountType.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'AccountType', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})

@login_required(login_url='login')
def Client_list_view(request):
    clients = Client.objects.all()
    return render(request,'Client/client_list.html',{'clients':clients})
