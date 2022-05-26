import csv

def save_to_csv(jobs):
  file = open('jobs.csv', 'w')
  write = csv.writer(file)
  write.writerow(['title', 'company', 'location', 'how_old', 'link'])

  for job in jobs:
    write.writerow(list(job.values()))


