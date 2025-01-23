import hashlib
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk, Kategori, Status
from .serializers import ProdukSerializer
from .forms import ProdukForm
from datetime import datetime

def fetch_and_save_data():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    
    current_date = datetime.today().strftime('%d-%m-%y')
    my_pass = 'bisacoding-' + current_date
    md5_hash = hashlib.md5(my_pass.encode()).hexdigest()

    data = {
        'username': 'tesprogrammer210125C21',
        'password': md5_hash
    }
    
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        data = response.json()
        
        for item in data['data']:
            kategori, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
            
            status, _ = Status.objects.get_or_create(nama_status=item['status'])
            
            Produk.objects.get_or_create(
                nama_produk=item['nama_produk'],
                harga=item['harga'],
                kategori=kategori,
                status=status
            )
    else:
        print(f"Error: {response.status_code} - {response.text}")

def product_list(request):
    fetch_and_save_data()
    produk = Produk.objects.filter(status__nama_status="bisa dijual").order_by('-id')
    # produk = Produk.objects.all().order_by('-id')
    return render(request, 'myapp/product_list.html', {'produk': produk})

def product_create(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProdukForm()
    return render(request, 'myapp/product_form.html', {'form': form})

def product_update(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'myapp/product_form.html', {'form': form})

def product_delete(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        produk.delete()
        return redirect('product_list')
    return render(request, 'myapp/product_confirm_delete.html', {'produk': produk})