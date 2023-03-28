from django.shortcuts import render, redirect
from django.contrib import messages
import openai
from .models import Past
from django.core.paginator import Paginator

# Create homepage
def home(request):
	# API Key: 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
	# Check for form submission 
	if request.method == "POST":
		question = request.POST['question']
		past_responses = request.POST['past_responses']
		#API Stuff
		openai.api_key = "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"

		#create OpenAI instance
		openai.Model.list()
		try:
			#Make a completion
			response = openai.Completion.create(
				model = "text-davinci-003",
				prompt = question,
				temperature=0,
				max_tokens=60,
				top_p=1.0,
				frequency_penalty=0.0,
				presence_penalty=0.0
			)

			#parse response
			response = (response["choices"][0]["text"]).strip()

			#logic for past responses
			if "3ff11c8f-bc21-4f6f-a8a9-a02bb2caae52" in past_responses:
				past_responses = response

			else:
				past_responses = f"{past_responses}<br/><br/>{response}"
				#save to DB
				record = Past(question=question, answer=response)
				record.save()
			return render(request, 'home.html', {"question": question, "response": response, "past_responses":past_responses})
		except Exception as e:
			return render(request, 'home.html', {"question": question, "response": e, "past_responses":past_responses})
	return render(request, 'home.html', {})

	
def past(request):
	#set up pagination
	p = Paginator(Past.objects.all(), 5)
	page = request.GET.get('page')
	pages = p.get_page(page)

	#query DB
	past = Past.objects.all()
	
	#Get number of pages
	nums = "a" * pages.paginator.num_pages

	return render(request, 'past.html', {"past":past, "pages":pages, "nums":nums})


def delete_past(request, Past_id):
	past = Past.objects.get(pk=Past_id)
	past.delete()
	messages.success(request, ("Record deleted"))




	return redirect('past')
