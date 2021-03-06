from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
  list_ = List.objects.get(id=list_id)
  error = None

  if request.method == 'POST':
    try:
      item = Item.objects.create(text=request.POST['item_text'], list=list_)
      item.full_clean()
      item.save()
      return redirect(list_)
    except ValidationError:
      error = "You can't have an empty list item"
      item.delete()

  return render(request, 'list.html', {'list': list_, 'error': error})

def new_list(request):
  list_ = List.objects.create()
  item = Item.objects.create(text=request.POST['item_text'], list=list_)
  try:
      item.full_clean()
      item.save()
  except ValidationError:
      error = "You can't have an empty list item"
      list_.delete()
      return render(request, 'home.html', {'error':error})

  return redirect(list_)

