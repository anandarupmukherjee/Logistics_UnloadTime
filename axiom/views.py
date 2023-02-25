from django.shortcuts import render
from axiom.models import Project, Project_buffer
from .models import QrCode
from django.http import HttpResponse
import os
from datetime import datetime
import time
import csv
import sqlite3
from jinja2 import Template


#import numpy as np

# Create your views here.
#def hello_world(request):
#	return render(request, 'hello_world.html', {})
def chk_tmfmt(dat):
    if dat=='':
        return '00:00'
    else:
        return dat
    

def tim_diff(d1,d2):
    
    if d1 and d2 == '':
        return 0.0
    else:
        FMT = '%H:%M'
        tdelta = datetime.strptime(chk_tmfmt(d2), FMT) - datetime.strptime(chk_tmfmt(d1), FMT)
        return tdelta.total_seconds()/60


def chk_neg(k):
    if k<0:
        a=0
    else:
        a=k 
    return a


def chk_work(ids,cont,total,w1,w2,w3,w4,w5,br1,br2,br3,br4,br5):
    for i in range(len(ids)):
        x=(w1,w2,w3,w4,w5)
        workers=5-x.count(0) #counts zero entries to determine how many workers were present
        w1x=chk_neg(w1-br1)
        w2x=chk_neg(w2-br2)
        w3x=chk_neg(w3-br3)
        w4x=chk_neg(w4-br4)
        w5x=chk_neg(w5-br5)
        tw=w1x+w2x+w3x+w4x+w5x #
        br=br1+br2+br3+br4+br5
    # print("--------------------")
    # print(ids,cont,total,workers,w1x,w2x,w3x,w4x,w5x,tw,br)
    # print("--------------------")

    return (ids,cont,total,workers,w1x,w2x,w3x,w4x,w5x,tw,br1,br2,br3,br4,br5,total-br)


def update(request):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        connection = sqlite3.connect('mydatabase')
        
        my_query=9
        cursor = connection.execute('SELECT id, order_id, container, product, customer, date_work FROM axiom_project WHERE id='+str(my_query)+";")

        # print("Polled data")
        
        # display row by row
        row_val=[]
        for row in cursor:
            # print(row)
            row_val.append(row)
        time.sleep(2)

        if request.method == 'POST':
            if request.POST.get('order_id') and request.POST.get('id'):
                # post=Project()
                pid= request.POST.get('id')
                order_id= request.POST.get('Order_id')
                # post.container= request.POST.get('container')
                date_work=request.POST.get('date_work')
                time_in=request.POST.get('time_in')
                time_out=request.POST.get('time_out')
                time_break_on=request.POST.get('time_break_on')
                time_break_off=request.POST.get('time_break_off')
                w1_start=request.POST.get('w1_start')
                w2_start=request.POST.get('w2_start')
                w3_start=request.POST.get('w3_start')
                w4_start=request.POST.get('w4_start')
                w5_start=request.POST.get('w5_start')
                w1_stop=request.POST.get('w1_stop')
                w2_stop=request.POST.get('w2_stop')
                w3_stop=request.POST.get('w3_stop')
                w4_stop=request.POST.get('w4_stop')
                w5_stop=request.POST.get('w5_stop')
                w1_break_on=request.POST.get('w1_break_on')
                w2_break_on=request.POST.get('w2_break_on')
                w3_break_on=request.POST.get('w3_break_on')
                w4_break_on=request.POST.get('w4_break_on')
                w5_break_on=request.POST.get('w5_break_on')
                w1_break_off=request.POST.get('w1_break_off')
                w2_break_off=request.POST.get('w2_break_off')
                w3_break_off=request.POST.get('w3_break_off')
                w4_break_off=request.POST.get('w4_break_off')
                w5_break_off=request.POST.get('w5_break_off')
                # supervisor=row_val[]
                # product=row_val[]
                # packages=row_val[]
                # sku=row_val[]
                # size=row_val[]
                # customer=row_val[]
                # container=row_val[]
                # date_work=row_val[]
                timestamp=dt_string
                # sql_query="""UPDATE axiom_project SET w1_start = '+str(w1_start)+', w1_stop = '+str(w1_stop)+' WHERE id = '+str(pid)+';"""
                



                # https://stackoverflow.com/questions/9236836/best-way-of-gluing-strings-in-python-to-compose-sql-query


                # cursor = connection.execute('UPDATE axiom_project SET container = "'"Test_anand"'" WHERE id = 9;')
                # connection.commit()
                # cursor.close()
                # print("all seems ok....")
                template_string = '''
                    UPDATE axiom_project
                    SET 
                        time_in = '{{time_in}}',
                        time_out = '{{time_out}}',
                        date_work = '{{date_work}}',
                        w1_start = '{{w1_start}}',
                        w1_stop = '{{w1_stop}}',
                        w1_break_on = '{{w1_break_on}}',
                        w1_break_off = '{{w1_break_off}}',
                        w2_start = '{{w2_start}}',
                        w2_stop = '{{w2_stop}}',
                        w2_break_on = '{{w2_break_on}}',
                        w2_break_off = '{{w2_break_off}}',
                        w3_start = '{{w3_start}}',
                        w3_stop = '{{w3_stop}}',
                        w3_break_on = '{{w3_break_on}}',
                        w3_break_off = '{{w3_break_off}}',
                        w4_start = '{{w4_start}}',
                        w4_stop = '{{w4_stop}}',
                        w4_break_on = '{{w4_break_on}}',
                        w4_break_off = '{{w4_break_off}}',
                        w5_start = '{{w5_start}}',
                        w5_stop = '{{w5_stop}}',
                        w5_break_on = '{{w5_break_on}}',
                        w5_break_off = '{{w5_break_off}}'

                    WHERE
                        id = {{id}}; 
                    '''


                params = {
                    'id': pid,
                    'time_in': time_in,
                    'time_out': time_out,
                    'date_work': date_work,
                    'w1_start': w1_start,
                    'w1_stop': w1_stop,
                    'w1_break_on': w1_break_on,
                    'w1_break_off': w1_break_off,
                    'w2_start': w2_start,
                    'w2_stop': w2_stop,
                    'w2_break_on': w2_break_on,
                    'w2_break_off': w2_break_off,
                    'w3_start': w3_start,
                    'w3_stop': w3_stop,
                    'w3_break_on': w3_break_on,
                    'w3_break_off': w3_break_off,
                    'w4_start': w4_start,
                    'w4_stop': w4_stop,
                    'w4_break_on': w4_break_on,
                    'w4_break_off': w4_break_off,
                    'w5_start': w5_start,
                    'w5_stop': w5_stop,
                    'w5_break_on': w5_break_on,
                    'w5_break_off': w5_break_off
                }

                output = Template(template_string).render(params)
                # print(output)


                connection = sqlite3.connect('mydatabase')
                cursor = connection.execute(output)
                connection.commit()
                cursor.close()
                # print("success")
        return render(request,'update.html', {'update':row_val})




def project_index(request):
    projects = Project.objects.all()
    buffer = Project_buffer.objects.all()
    test_analysis()
    return render(request, 'project_index.html', {'projects': projects, 'buffer': buffer})


def project_detail(request, pk):
    fin_all=[]
    project = Project.objects.get(pk=pk)
    x1_br= tim_diff(project.w1_break_on,project.w1_break_off)
    x2_br= tim_diff(project.w2_break_on,project.w2_break_off)
    x3_br= tim_diff(project.w3_break_on,project.w3_break_off)
    x4_br= tim_diff(project.w4_break_on,project.w4_break_off)
    x5_br= tim_diff(project.w5_break_on,project.w5_break_off)
    x= tim_diff(project.time_in,project.time_out)
    w1=tim_diff(project.w1_start, project.w1_stop)
    w2=tim_diff(project.w2_start, project.w2_stop)
    w3=tim_diff(project.w3_start, project.w3_stop)
    w4=tim_diff(project.w4_start, project.w4_stop)
    w5=tim_diff(project.w5_start, project.w5_stop)
    unload_time_order=x
    x_br=x1_br+x2_br+x3_br+x4_br+x5_br
    unload_time_accurate=x-x_br
    fin=chk_work(project.order_id,project.container,unload_time_order,w1,w2,w3,w4,w5,x1_br,x2_br,x3_br,x4_br,x5_br)
    #(ids,cont,total,workers,w1x,w2x,w3x,w4x,w5x )
    # print(x_br)
#    buffer = Project_buffer.objects.get(order_id='yet2200')
#    project = Project.objects.all()
    context = {
        'project': project,
        'tot_tim':fin[2],
        'w1_t':fin[4],
        'w2_t':fin[5],
        'w3_t':fin[6],
        'w4_t':fin[7],
        'w5_t':fin[8],
         'men':fin[3],
         'tw':fin[9]/60,
         'brk1':fin[10],
         'brk2':fin[11],
         'brk3':fin[12],
         'brk4':fin[13],
         'brk5':fin[14],
         'effect_work':fin[15],
         'sum_break':x_br
#        'buffer': buffer
    }
    return render(request, 'project_detail.html', context)


def home(request):
    if request.method=="POST":
        Url=request.POST['url']
        QrCode.objects.create(url=Url)
        qr_code=QrCode.objects.all()
    else:
        qr_code=None
    return render(request,"home.html",{'qr_code':qr_code})


def admin(request):
    return render(request,"admin.html")



def createpost(request):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(2)
        if request.method == 'POST':
            if request.POST.get('order_id') and request.POST.get('container'):
                post=Project()
                post.order_id= request.POST.get('order_id')
                post.container= request.POST.get('container')
                post.date_work=request.POST.get('date_work')
                # post.time_in=request.POST.get('time_in')
                # post.time_out=request.POST.get('time_out')
                # post.time_break_on=request.POST.get('time_break_on')
                # post.time_break_off=request.POST.get('time_break_off')
                # post.w1_start=request.POST.get('w1_start')
                # post.w2_start=request.POST.get('w2_start')
                # post.w3_start=request.POST.get('w3_start')
                # post.w4_start=request.POST.get('w4_start')
                # post.w5_start=request.POST.get('w5_start')
                # post.w1_stop=request.POST.get('w1_stop')
                # post.w2_stop=request.POST.get('w2_stop')
                # post.w3_stop=request.POST.get('w3_stop')
                # post.w4_stop=request.POST.get('w4_stop')
                # post.w5_stop=request.POST.get('w5_stop')
                # post.w1_break_on=request.POST.get('w1_break_on')
                # post.w2_break_on=request.POST.get('w2_break_on')
                # post.w3_break_on=request.POST.get('w3_break_on')
                # post.w4_break_on=request.POST.get('w4_break_on')
                # post.w5_break_on=request.POST.get('w5_break_on')
                # post.w1_break_off=request.POST.get('w1_break_off')
                # post.w2_break_off=request.POST.get('w2_break_off')
                # post.w3_break_off=request.POST.get('w3_break_off')
                # post.w4_break_off=request.POST.get('w4_break_off')
                # post.w5_break_off=request.POST.get('w5_break_off')
                post.supervisor=request.POST.get('supervisor')
                post.product=request.POST.get('product')
                post.packages=request.POST.get('packages')
                post.sku=request.POST.get('sku')
                post.size=request.POST.get('size')
                post.customer=request.POST.get('customer')
                post.timestamp=dt_string
                post.save()
            return render(request, 'createpost.html')  

        else:
                return render(request,'createpost.html')



def analysis(request):
    labels = []
    data = []
    order = []
    work = []
    w1=[]
    w2=[]
    w3=[]
    w4=[]
    w5=[]
    tw=[]

    queryset = Project_buffer.objects.order_by('-container')
    for orders in queryset:
        labels.append(orders.container)
        data.append(orders.unload_time)
        work.append(orders.workers)
        order.append(orders.order_id)
        w1.append(orders.w1)
        w2.append(orders.w2)
        w3.append(orders.w3)
        w4.append(orders.w4)
        w5.append(orders.w5)
        tw.append(orders.tw)

    return render(request, 'analysis.html', {
        'labels': labels,
        'data': data,
        'work': work,
        'id': order,
        'w1':w1,
        'w2':w2,
        'w3':w3,
        'w4':w4,
        'w5':w5,
        'tw':tw,
    })



def summary(request):

    fin_all=[]
    Project_buffer.objects.all().delete()

    queryset = Project.objects.order_by('-timestamp')
    for orders in queryset:
        orderids=orders.order_id
        container=orders.container
        x1_br= tim_diff(orders.w1_break_on,orders.w1_break_off)
        x2_br= tim_diff(orders.w2_break_on,orders.w2_break_off)
        x3_br= tim_diff(orders.w3_break_on,orders.w3_break_off)
        x4_br= tim_diff(orders.w4_break_on,orders.w4_break_off)
        x5_br= tim_diff(orders.w5_break_on,orders.w5_break_off)
        x= tim_diff(orders.time_in,orders.time_out)
        w1=tim_diff(orders.w1_start, orders.w1_stop)
        w2=tim_diff(orders.w2_start, orders.w2_stop)
        w3=tim_diff(orders.w3_start, orders.w3_stop)
        w4=tim_diff(orders.w4_start, orders.w4_stop)
        w5=tim_diff(orders.w5_start, orders.w5_stop)
        unload_time_order=x
        fin=chk_work(orderids,container,unload_time_order,w1,w2,w3,w4,w5,x1_br,x2_br,x3_br,x4_br,x5_br)
        #print(fin)
        #Project_buffer.objects.all().delete()
        pt=Project_buffer()
        pt.order_id=fin[0]
        pt.container=fin[1]
        pt.unload_time=fin[2]
        pt.workers=fin[3]
        pt.w1=fin[4]
        pt.w2=fin[5]
        pt.w3=fin[6]
        pt.w4=fin[7]
        pt.w5=fin[8]
        pt.tw=fin[9]/60
        pt.br1=fin[10]
        pt.br2=fin[11]
        pt.br3=fin[12]
        pt.br4=fin[13]
        pt.br5=fin[14]
        pt.save()
       #print(orders.order_id+"  "+str(x))
       # print(fin)
    buffer = Project_buffer.objects.all()

    # connection = sqlite3.connect('mydatabase')
    # my_query=1379310
    # cursor = connection.execute('SELECT container, product, customer, date_work FROM axiom_project WHERE order_id='+str(my_query)+";")
    # print("Polled data")
    
    # # display row by row
    # row_val=[]
    # for row in cursor:
    #     print(row)
    #     row_val.append(row)

    return render(request, 'summary.html', {'buffer': buffer})



def test_analysis():

    fin_all=[]

    queryset = Project.objects.order_by('-customer')
    for orders in queryset:
        orderids=orders.order_id
        container=orders.container
        x1_br= tim_diff(orders.w1_break_on,orders.w1_break_off)
        x2_br= tim_diff(orders.w2_break_on,orders.w2_break_off)
        x3_br= tim_diff(orders.w3_break_on,orders.w3_break_off)
        x4_br= tim_diff(orders.w4_break_on,orders.w4_break_off)
        x5_br= tim_diff(orders.w5_break_on,orders.w5_break_off)
        x= tim_diff(orders.time_in,orders.time_out)
        w1=tim_diff(orders.w1_start, orders.w1_stop)
        w2=tim_diff(orders.w2_start, orders.w2_stop)
        w3=tim_diff(orders.w3_start, orders.w3_stop)
        w4=tim_diff(orders.w4_start, orders.w4_stop)
        w5=tim_diff(orders.w5_start, orders.w5_stop)
        unload_time_order=x
        fin=chk_work(orderids,container,unload_time_order,w1,w2,w3,w4,w5,x1_br,x2_br,x3_br,x4_br,x5_br)
        # print(fin)






def analysis1(request):
    labels = []
    data = []
    diff = []

    queryset = Project.objects.order_by('-supervisor')
    for orders in queryset:
        labels.append(orders.supervisor)
        data.append(orders.order_id)
        s2 = orders.time_out
        s1 = orders.time_in
        FMT = '%H:%M'
        tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
        diff.append(tdelta.total_seconds()/60)
        #print(tdelta.total_seconds()/60)
    # print(diff)
    return render(request, 'analysis1.html', {
        'labels': labels,
        'data': diff,
    })


def analysis2(request):
    labels = []
    data = []
    diff = []

    queryset = Project.objects.order_by('-timestamp')
    for orders in queryset:
        labels.append(orders.order_id)
        data.append(orders.packages)
        s2 = orders.time_out
        s1 = orders.time_in
        FMT = '%H:%M'
        tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
        diff.append(tdelta.total_seconds()/60)
        #print(tdelta.total_seconds()/60)

    return render(request, 'analysis2.html', {
        'labels': labels,
        'data': diff,
        'data1': data,
    })


def csv_database_write(request):
    unload_time_order=[]
    orderids=[]
    w1=[]
    w2=[]
    fin=[]
    # Get all data from UserDetail Databse Table
    users = Project.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_database_write.csv"'
    writer = csv.writer(response)
    writer.writerow(['timestamp', 'order-id', 'customer', 'container_id',  'container_size', 'packages', 'sku', 'unload_time(m)', 'Workers', 'Person hours (mins.)', 'Collective break hours (mins.)'])

    for user in users:
        orderids.append(user.order_id)
        s2 = user.time_out
        s1 = user.time_in
        FMT = '%H:%M'
        tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
        x1_br= tim_diff(user.w1_break_on,user.w1_break_off)
        x2_br= tim_diff(user.w2_break_on,user.w2_break_off)
        x3_br= tim_diff(user.w3_break_on,user.w3_break_off)
        x4_br= tim_diff(user.w4_break_on,user.w4_break_off)
        x5_br= tim_diff(user.w5_break_on,user.w5_break_off)
        x_br=x1_br+x2_br+x3_br+x4_br+x5_br
        unload_time_order= tdelta.total_seconds()/60
        w1=tim_diff(user.w1_start, user.w1_stop)
        w2=tim_diff(user.w2_start, user.w2_stop)
        w3=tim_diff(user.w3_start, user.w3_stop)
        w4=tim_diff(user.w4_start, user.w4_stop)
        w5=tim_diff(user.w5_start, user.w5_stop)
        fin=chk_work(user.order_id,user.container,unload_time_order,w1,w2,w3,w4,w5,x1_br,x2_br,x3_br,x4_br,x5_br)
        #w1= (datetime.strptime(user.w1_stop, FMT) - datetime.strptime(user.w1_start, FMT)).total_seconds()/60
        #w2= (datetime.strptime(user.w2_stop, FMT) - datetime.strptime(user.w2_start, FMT)).total_seconds()/60
        #print(unload_time_order)
        writer.writerow([user.timestamp, user.order_id, user.customer, user.container, user.size, user.packages, user.sku, unload_time_order, fin[3], fin[9], x_br])
    return response








