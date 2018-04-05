import urllib, json

class Selic:
  date  = ''
  value = 0
  rate  = 0.0

  def __init__(self):
    url = "http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
    response = urllib.urlopen(url)
    data  = json.loads(response.read())
    self.value = data[len(data) - 1]["valor"]
    self.date  = data[len(data) - 1]["data"]
    for i in range(1, 30, 1):
      self.rate += float(data[len(data) - i]["valor"])

  def getValue(self):
    return self.value

  def getDate(self):
    return self.date