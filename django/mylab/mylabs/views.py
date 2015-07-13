from django.shortcuts import render
from django.views.generic import TemplateView

import RPi.GPIO as GPIO

class LedPageView(TemplateView):
    template_name = "mylab/led.html"

    def dispatch(self, request, *args, **kwargs):
        self.bool = kwargs.get('bool', None)
        self.pin = kwargs.get('pin', None)
        if self.bool == 'no':
            print self.led_turnoff()
        if self.bool == 'si':
            #print self.led_turnoff()
            print self.led_turnon(self.pin)
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


