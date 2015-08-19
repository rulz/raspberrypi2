# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

import RPi.GPIO as GPIO
import time
import json
import random
from scripts import ultrasonido

class LedPageView(TemplateView):
    template_name = "mylab/led.html"

    def dispatch(self, request, *args, **kwargs):
        self.bool = kwargs.get('bool', None)
        self.pin = kwargs.get('pin', None)
        if self.bool == 'no':
            self.led_turnoff()
        if self.bool == 'si':
            #print self.led_turnoff()
            self.led_turnon(self.pin)
        return super(LedPageView, self).dispatch(request, *args, **kwargs)
   
    def led_turnon(self, pin):
        GPIO.setmode(GPIO.BCM)
        if pin:
            pin = int(pin)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, True)
        return True
        
    def led_turnoff(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        return False
    
    def get_context_data(self, **kwargs):
        context = super(LedPageView, self).get_context_data(**kwargs)
        context['pins'] = range(1, 28)
        return context
led_page = LedPageView.as_view()

class UltraPageView(TemplateView):
    template_name = "mylab/ultra.html"

    def dispatch(self, request, *args, **kwargs):
        self.bool = kwargs.get('bool', None)
        self.pin = kwargs.get('pin', None)
        if self.bool == 'no':
            self.ultra_turnoff()
        # if self.bool == 'si':
        #     self.ultra_turnon()
        return super(UltraPageView, self).dispatch(request, *args, **kwargs)
        
    def ultra_turnoff(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        return HttpResponseRedirect(reverse('ultra_page'))

    #nose si crear un json aca
    def on_ultrasonido(self):
        ultrasonido()
        return
    
    def get_context_data(self, **kwargs):
        context = super(UltraPageView, self).get_context_data(**kwargs)
        context['pins'] = range(1, 28)
        return context
ultra_page = UltraPageView.as_view()

class GetUltraSonido(View):
    def get(self, request):
        # num = random.randrange(10)
        # print num, 'siii'
        num = ultrasonido()
        json_response = {
            'num': num
        }
        GPIO.cleanup()
        return HttpResponse(
            json.dumps(json_response),
            content_type="application/json;charset=utf-8"
        )

get_ultrasonido = GetUltraSonido.as_view()

class LuzPageView(TemplateView):
    template_name = "mylab/luz.html"

    def dispatch(self, request, *args, **kwargs):
        self.bool = kwargs.get('bool', None)
        self.pin = kwargs.get('pin', None)
        if self.bool == 'no':
            self.ultra_turnoff()
        if self.bool == 'si':
            self.luz_turnon(self.pin)
        return super(LuzPageView, self).dispatch(request, *args, **kwargs)
        
    def ultra_turnoff(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        return HttpResponseRedirect(reverse('luz_page'))

    def luz_turnon(self, pin):
        GPIO.setmode(GPIO.BCM)
        if pin:
            pin = int(pin)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, True)
        return True

luz_page = LuzPageView.as_view()

