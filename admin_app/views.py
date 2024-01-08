from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from admin_app.db_collection import get_collection
from bson import ObjectId
import numpy as np

def fetch_jobs():
    collection = get_collection()
    print("Getting data from db...")
    cursor = collection.find()
    return cursor

def index(request):
    page = request.GET.get('page', 1)
    per_page = 15
    cursor = fetch_jobs()
    jobs = []
    for job in cursor:
        job['id'] = str(job.pop('_id'))
        jobs.append(job)

    paginator = Paginator(jobs, per_page)
    try:
        paginated_jobs = paginator.page(page)
    except PageNotAnInteger:
        paginated_jobs = paginator.page(1)
    except EmptyPage:
        paginated_jobs = paginator.page(paginator.num_pages)
    
    context = {
        'jobs': paginated_jobs,
        'totalJobs':len(jobs),
        'perPage':per_page
    }

    return render(request, 'index.html',context)

def Update(request,id):
    if request.method == "POST":
        job_company = request.POST.get('job_company')
        job_title = request.POST.get('job_title')
        job_location = request.POST.get('job_location')
        job_salary = request.POST.get('job_salary')

        collection = get_collection()
        collection.update_one({'_id':ObjectId(id)},{'$set':{
            "job_company":job_company,
            "job_location":job_location,
            "job_salary":int(job_salary),
            "job_title":job_title
        }})
        return redirect('home')

    return redirect(request, 'index.html')


def Delete(request,id):
    collection = get_collection()
    delete= collection.delete_one({'_id':ObjectId(id)})
    return redirect('home')


def average_salary(request):
    cursor = fetch_jobs()
    cursor1 = fetch_jobs()
    # print([entry['job_location'] for entry in cursor])
    locations = np.array([entry['job_location'] for entry in cursor])
    salaries = np.array([entry['job_salary'] for entry in cursor1])
    non_zero_salaries = salaries[salaries != 0]
    mean_salary = np.mean(non_zero_salaries)
    salaries[salaries == 0] = mean_salary

    # Create a dictionary to store the sum and count of salaries for each location
    location_stats = {}
    for location, salary in zip(locations, salaries):
        if location not in location_stats:
            location_stats[location] = {'sum': 0, 'count': 0}
        location_stats[location]['sum'] += salary
        location_stats[location]['count'] += 1

    # Calculate the mean salary for each location
    average_salary_by_location = {location: stats['sum'] / stats['count'] for location, stats in location_stats.items()}
    context = {
        'averageSalary': mean_salary,
        'averageSalaryByLocation':average_salary_by_location
    }
    return render(request, 'average.html',context)