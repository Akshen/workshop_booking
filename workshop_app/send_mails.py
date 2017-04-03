from django.core.mail import send_mail
from workshop_portal.settings import (
                    EMAIL_HOST, 
                    EMAIL_PORT, 
                    EMAIL_HOST_USER, 
                    EMAIL_HOST_PASSWORD,
                    EMAIL_USE_TLS
                    )

def send_email(request, call_on, user_position=None):
	'''
	Email sending function while registration and 
	booking confirmation.
	'''

	if call_on == 'Registration':
		if user_position == 'instructor':
			message = 'Thank You for Registering on this platform. \n \
						Since you have ask for Instructor Profile, \n \
						we will get back to you soon after verifying your \n \
						profile. \
						In case if you don\'t get any response within 3days, \
						Please contact us at   '
			send_mail(
					'Welcome to FOSSEE', message, EMAIL_HOST_USER, 
					[request.user.email], fail_silently=False
					)
			#Send a mail to admin as well as a notification.
		else:
			message = 'Thank You for Registering on this platform.\n \
						Rules. \n \ If you face any issue during \
						 your session please contact fossee.'
			send_mail(
					'Welcome to FOSSEE', message, EMAIL_HOST_USER, 
					[request.user.email], fail_silently=False
					)

	elif call_on == 'Booking':
		if user_position == 'instructor':
			message = 'You got a workshop booking request \
						from user name '
			send_mail(
					'Python Workshop Booking | FOSSEE', message, EMAIL_HOST_USER, 
					[request.user.email], fail_silently=False
					)

		else:
			message = 'Thank You for Booking on this platform.\n \
						Rules to be added \
					If you face any issue during your session please contact \
					fossee.'
			send_mail(
					'Python Workshop Booking | FOSSEE', message, EMAIL_HOST_USER, 
					[request.user.email], fail_silently=False
					)
