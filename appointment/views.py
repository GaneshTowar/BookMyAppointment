from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from userprofile.models import Profile
from reg.models import regis
import random
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')


def logregc(request):
    return render(request, "logregc.html")


def logregp(request):
    return render(request, "logregp.html")


def cregs(request):  # registration of the client
    if request.method == 'POST':
        username = request.POST['crusername']
        email = request.POST['cremail']
        password = request.POST['crpassword']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
            return redirect('/logregc')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            auth.login(request, user)
            messages.info(request, 'user created')
            return render(request, 'chome.html')
    else:
        return render(request, 'logregc.html')


def clogs(request):  # login of the client

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'chome.html')
        else:
            return redirect('/logregc')
    else:
        return redirect('/logregc')


def pregs(request):  # registration of the service pro
    if request.method == 'POST':
        username = request.POST['srusername']
        email = request.POST['sremail']
        password = request.POST['srpassword']
        occupation = request.POST['occupation']
        opensat = request.POST['opensat']
        closesat = request.POST['closesat']
        duration = request.POST['duration']
        fee = request.POST['fees']
        city = request.POST['city']
        address = request.POST['address']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
            print('username taken')
            return redirect('/logregp')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            p = Profile()
            p.user = user
            p.city = city
            p.opensat = opensat
            p.closesat = closesat
            p.duration = duration
            p.visitfee = fee
            p.occupation = occupation
            p.serviceprovider = True
            p.address = address
            p.save()
            auth.login(request, user)
            print('user created')
            messages.info(request, 'user created')
            return render(request, 'phome.html')
    else:
        return render(request, 'logregc.html')


def plogs(request):  # login of the service pro
    if request.method == 'POST':
        username = request.POST['slusername']
        password = request.POST['slpassword']

        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        if user is not None:
            auth.login(request, user)
            appons = regis.objects.filter(sp=request.user, stat='accepted')
            data = {
                'appons': appons
            }
            return render(request, 'phome.html', data)
        else:
            return redirect('/logregp')
    else:
        return redirect('/logregp')


def req(request):
    if request.user is not None:
        appons = regis.objects.filter(sp=request.user, stat='pending')
        data = {
            'appons': appons
        }
        return render(request, 'req.html', data)
    else:
        return '404 error : user not logged in '


def listsp(request):
    # city aur type of service pata karenge aur ek service providers ki list bhejenge
    city = request.POST['city']
    service = request.POST['service']
    serpros = Profile.objects.filter(city=city, occupation=service)
    data = {
        'serpros': serpros
    }
    return render(request, 'listsp.html', data)


def approach(request, id):
    udata = Profile.objects.get(user_id=id)
    idd = udata.user_id
    opens = udata.opensat
    closes = udata.closesat
    duration = udata.duration
    openhr = opens.hour * 60
    openmin = opens.minute
    closeshr = closes.hour * 60
    closesmin = closes.minute
    totopen = openhr + openmin
    totclose = closeshr + closesmin
    a = []
    while totopen < totclose:
        tot = totopen / 60
        if tot > 12:
            tot = tot - 12
            if (tot % 1) > 0:
                ratio = tot % 1
                tot = (tot - ratio) + ((60 * ratio) / 100)
                tot = str(tot)
                tot = tot + '0 PM'
                a.append(tot)
            else:
                tot = str(tot)
                tot = tot +'0 PM'

                a.append(tot)
        else:
            if (tot % 1) > 0:
                ratio = tot % 1
                tot = (tot - ratio) + ((60 * ratio) / 100)
                tot = str(tot)
                tot = tot + '0 AM'
                a.append(tot)
            else:
                tot = str(tot)
                tot = tot + '0 AM'
                a.append(tot)

        totopen = totopen + duration

    print(a)
    data = {
        'udata': udata,
        'a': a
    }
    return render(request, 'approach.html', data)


def apemail(request, id):
    udata = Profile.objects.get(user_id=id)
    r = regis()
    r.appointment_opt = random.randint(100000, 999999)
    r.cl = request.user
    r.sp = udata.user
    r.date = request.POST['date']
    r.time = request.POST['time']
    r.stat = 'pending'
    r.save()
    sname = udata.user.username

    d = {
        'udata': sname
    }
    return render(request, 'apemail.html', d)


def Logout(request):
    logout(request)
    return render(request, 'home.html')


def accept(request, id):
    r = regis.objects.get(id=id)
    r.stat = 'accepted'
    r.save()
    r1 = regis.objects.get(id=id)
    nm = r1.sp.username
    tym = r1.time
    vc = r1.appointment_opt
    date = r1.date
    ml = r1.cl.email
    mes = f'your appointment with {nm} has been confirmed your verfication code is{vc} ,appointment timing is {r1.date} {tym}'
    send_mail(
        f'BookMyAppointment CODE{vc}',
        f'{mes}',
        '20210804001@dypiu.ac.in',
        [f'{ml}'],

    )
    return redirect('/req')


def decline(request, id):

    r = regis.objects.get(id=id)
    r.stat = 'decline'
    nm= r.sp.username
    ml= r.cl.email
    mes = f'you appointment with{nm} has been rejected '
    send_mail(
        'BookMyAppointment',
        f'{mes}',
        '20210804001@dypiu.ac.in',
        [f'{ml}'],

    )
    r.save()
    return redirect('/req')


def upcomap(request):
    if request.user is not None:
        appons = regis.objects.filter(sp=request.user, stat='accepted')
        data = {
            'appons': appons
        }
        return render(request, 'phome.html', data)


def complete(request,id):
    appo = regis.objects.get(id=id)
    appo.delete()
    return redirect('/upcomap')

def ccomplete(request,id):
    appo = regis.objects.get(id=id)
    appo.delete()
    return redirect('/myappointments')

def myappointments(request):
    if request.user is not None:
        appons = regis.objects.filter(cl=request.user)
        data = {
            'appons': appons
        }
        return render(request, 'myappointments.html', data)
    else:
        return '404 error : user not logged in '

def bookappointments(request):
    if request.user is not None :
        return render(request, 'chome.html')

