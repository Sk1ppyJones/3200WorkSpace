from django.shortcuts import render

HOLIDAYS = {
    "January": [
        "New Year's Day (Jan 1)",
        "Martin Luther King Jr. Day (Third Monday)"
    ],
    "February": [
        "Groundhog Day (Feb 2)",
        "Valentine's Day (Feb 14)",
        "Washington's Birthday / Presidents' Day (Third Monday)"
    ],
    "March": [
        "St. Patrick's Day (Mar 17)",
        "Easter (Date varies)"
    ],
    "April": [
        "April Fool's Day (Apr 1)",
        "Easter (Date varies)"
    ],
    "May": [
        "Cinco de Mayo (May 5)",
        "Mother's Day (Second Sunday)",
        "Memorial Day (Last Monday)"
    ],
    "June": [
        "Juneteenth National Independence Day (Jun 19)",
        "Father's Day (Third Sunday)",
        "Flag Day (Jun 14)"
    ],
    "July": [
        "Independence Day (Jul 4)"
    ],
    "August": [],
    "September": [
        "Labor Day (First Monday)",
        "Grandparents Day (Second Sunday)"
    ],
    "October": [
        "Columbus Day (Second Monday)",
        "Indigenous People's Day (Second Monday)",
        "Halloween (Oct 31)"
    ],
    "November": [
        "Veterans Day (Nov 11)",
        "Thanksgiving Day (Fourth Thursday)",
        "Black Friday (Day after Thanksgiving)"
    ],
    "December": [
        "Christmas Day (Dec 25)",
        "New Year's Eve (Dec 31)",
        "Hanukkah (Date varies)",
        "Kwanzaa (Dec 26 - Jan 1)"
    ]
}


# Create your views here.
def index(request):
    context = {
        "months": HOLIDAYS.keys()
    }
    return render(request, 'holidays/index.html', context)


def month_detail(request, month):
    holidays = HOLIDAYS.get(month.title(), [])
    
    context = {
        "month": month.title(),
        "holidays": holidays,
    }
    return render(request, 'holidays/month_detail.html', context)
