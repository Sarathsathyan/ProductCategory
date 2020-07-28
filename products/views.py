from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Category,Products
# Create your views here.
def index(request):


    if request.method == 'POST':
        if 'category' in request.POST:
            name = request.POST['name']
            cate_image = request.FILES.get('cate_image')
            category = Category(cate_name=name,cate_image=cate_image)
            category.save()

        if 'product_submit' in request.POST:
            cate_name = request.POST['cate_name']
            prod_name = request.POST['prod_name']
            pro_image = request.FILES.get('prod_image')
            pro_price = request.POST['prod_price']
            pro_features = request.POST['cfp_course']
            prod_description = request.POST['pro_descrip']
            cat_id = Category.objects.get(id=cate_name)
            print(cat_id)

            product =  Products(cate_name=cat_id.cate_name,pro_name=prod_name,pro_image=pro_image,produ_features=pro_features,
                                product_price=pro_price,prod_description=prod_description,c_id=cat_id)
            product.save()


    category_list = Category.objects.all()
    prod_list = Products.objects.order_by("-product_create_date")
    context ={
        'category_list':category_list,
        'prod_list' : prod_list
    }
    return render(request, 'products/index.html',context)


def CategoryEdit(request,id):
    cfp_id=id
    datas=Category.objects.get(id=cfp_id)

    if request.method == 'POST':
        if 'category_submit' in request.POST:
            new_category = request.POST['category_name']
            datas = Category.objects.get(id=id)
            datas.cate_name = new_category
            datas.save()
        if 'change_img' in request.POST:
            i_id = request.POST['idd']
            cate_img = request.FILES.get('pro_image')
            datas = Category.objects.get(id=i_id)
            datas.cate_image  = cate_img
            datas.save()
            return redirect('category_edit',cfp_id)
    context ={
        'datas': datas
    }

    return render(request,"products/categoryEdit.html",context)



def productEdit(request,id):
    p_id = id
    datas = Products.objects.get(id=p_id)
    category_list = Category.objects.all()
    feature_str=datas.produ_features
    feature_list=feature_str.split('_')

    if request.method == 'POST':
        if 'pro_submit' in request.POST:
            pro_name = request.POST['pro_name']
            pro_price = request.POST['pro_price']
            pro_descrip= request.POST['pro_descrip']
            pro_feature = request.POST['cfp_course']


            details = Products.objects.get(id = p_id)
            details.pro_name = pro_name
            details.product_price = pro_price
            details.prod_description = pro_descrip
            details.produ_features = pro_feature

            details.save()
            return redirect('product_edit',p_id)
        if 'change_img' in request.POST:
            pro_image = request.FILES.get('pro_image')
            details = Products.objects.get(id=p_id)
            details.pro_image = pro_image
            details.save()
            return redirect('product_edit',p_id)


        if 'pro_delete' in request.POST:
            del_id = request.POST['delete_id']
            obj = Products.objects.filter(id=del_id)
            obj.delete()
            return redirect('index')



    context={
        'datas':datas,
        'role_list':feature_list,
        'category_list':category_list,
    }

    return render(request,'products/product_edit.html',context)
