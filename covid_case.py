import requests
from mail_module import Gmail
import time

# https://api.covid19tracker.ca/docs/1.0/regions

class getCovidUpdate:
  def __init__(self):
      print("init") # never prints

  def getData(self):    
    data = requests.get('https://api.covid19tracker.ca/reports/province/on').json()['data']
    a = 'Convid 19 (Ontario) - Daily report \n'
    for n in range(1,4):
      a = a + '\n' + data[-n]['date'] + ':  '+  str(data[-n]['change_cases'])
    return a 
    # 
    # email.send()

  def run(self):
    result = self.getData()
    email = Gmail('ling.duke@gmail.com', 'Covid update', result)
    email.send()
    print('Covid update App is running...')
    while True:
      time.sleep(60*60)
      update = self.getData()
      if result != update:
        result = update
        updateEmail = Gmail('ling.duke@gmail.com', 'Covid update', update)
        updateEmail.send()
        print('Covid update App has updated...')

if __name__ == '__main__':
  app = getCovidUpdate()
  app.run()


