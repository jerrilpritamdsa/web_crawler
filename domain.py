from urllib.parse import urlparse

#get domain name(examkple.com)
def get_domain_name(url):
    try:
        results=get_sub_domain_name(url).split('.')
        return results[-2]+ '.'+ results[-1]

    except:
        return ''

#geting sub domain name(mail.example.com)
#but we only need (example.com) so see the above function
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
