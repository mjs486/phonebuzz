from django.shortcuts import render
from django.http import HttpResponse
from twilio import twiml

def fizzbuzz(n1,n2,N):

	def lcm(a, b):
		def gcd(a,b):
		    while b > 0:
		        a,b = b,a%b
		    return a 
		return a*b/gcd(a,b)

	n3 = lcm(n1,n2)
	fizzbuzz_list = [n1,n2,n3];
	fizzbuzz_map = {n1:'Fizz',n2:'Buzz',n3:'Fizz Buzz'}

	output_list = [str(x) for x in range(1,N+1)]

	for val in fizzbuzz_list:
		for i in range(val,N+1,val):
			output_list[i-1] = fizzbuzz_map[val]
	return(' '.join(output_list))

def index(request):
	resp = twiml.Response()
	resp.say(fizzbuzz(3,5,30))
	print(resp)
	return HttpResponse(resp)