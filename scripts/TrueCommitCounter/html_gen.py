from jinja2 import Template
from github import Github
from datetime import datetime
from pathlib import Path
import os
import shutil

construct_grid = dict()
date_grid = dict()

filepath = Path(__file__).resolve().parent
print("Running script in directory: " + str(filepath))

with open(f'{filepath}/basic_details.csv','r') as data_file:
    for data in data_file.readlines():
        line = data.split(',')
        repo_name = line[0]
        branch = line[1]
        date = datetime.strptime(line[2],"%Y-%m-%d %H:%M:%S")
        date_of_year = int(date.strftime("%j"))
        commit_hash_uri = line[3].rstrip()
        if date.year not in construct_grid:
            construct_grid[date.year] = dict()
            date_grid[date.year] = dict()
        if date_of_year not in construct_grid[date.year]:
            construct_grid[date.year][date_of_year] = []
            date_grid[date.year][date_of_year] = ''
        stripped_hash = commit_hash_uri.split('/commit/')[1][:6]
        construct_grid[date.year][date_of_year].append([repo_name, branch, stripped_hash])
        date_grid[date.year][date_of_year] = date.strftime("%d/%m/%Y")

years = [2017, 2018, 2019, 2020, 2021, 2022]

for year in years:
    for i in range(1,366):
        if i not in construct_grid[year]:
            construct_grid[year][i] = []
            date_grid[year][i] = datetime.strptime(f'{year} {i}', '%Y %j').strftime("%d/%m/%Y")

# print(construct_grid)

html_code_template = '''
<h1>True Commit Counter</h1>
<p>Github Contributions doesn't count contributions made to fork of forks (ports of webkit in my case) Hence wrote a scrapper to get accurate commit history.</p>
<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h4 class="modal-title" id="myModalLabel">Modal title</h4>
      </div>
      <div style="margin:5px" class="modal-body-gh">
        ...
      </div>
       <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
{% for year in years %}
<div class="container{{year}}">
<h2>{{year}}</h2>
<hr/>
<div class="graph">
    <ul class="months">
      <li>Jan</li>
      <li>Feb</li>
      <li>Mar</li>
      <li>Apr</li>
      <li>May</li>
      <li>Jun</li>
      <li>Jul</li>
      <li>Aug</li>
      <li>Sep</li>
      <li>Oct</li>
      <li>Nov</li>
      <li>Dec</li>
    </ul>
    <ul class="days">
      <li>Sun</li>
      <li>Mon</li>
      <li>Tue</li>
      <li>Wed</li>
      <li>Thu</li>
      <li>Fri</li>
      <li>Sat</li>
    </ul>
    <ul class="squares{{year}}">
      <!-- added via javascript -->
    </ul>
  </div>
  </div>
{% endfor %}
<script>
$(document).ready(function(){
  // $('[data-toggle="tooltip-gh"]').tooltip();
  $('.dropdown-gh').mouseover(function() {
        $('[data-toggle="tooltip-gh"]').tooltip();
    })
  $('.dropdown-gh').click(function() {
       var content = $(this).attr('data-list');
       const array = JSON.parse(content.replace(/'/g, '"'));
       var cleaned_data = '';
       for(let i=0; i< array.length; i++){
           cleaned_data+= `<p>${array[i][0]}(branch:${array[i][1]}) commit:<a target="_blank" href='https://github.com/${array[i][0]}/commit/${array[i][2]}'>${array[i][2]}</a></p>`;
       }
       $('#myModalLabel').text($(this).attr('data-original-title'));
       $('.modal-body-gh').html(cleaned_data);
       $('#myModal').modal('show');
    })
});
</script>
<script>
    {% for year in years %}
        const squares{{ year }} = document.querySelector('.squares{{ year }}');
        {% for i in range(1,366) -%}
        {% set weight = grid_data[year][i] | length -%}
        {% if weight==0 -%}
            {% set color = '#ebedf0' -%}
        {% elif weight>=1 and weight<=5 -%}
            {% set color = '#c6e48b' -%}
        {% elif weight>=6 and weight<=15 -%}
            {% set color = '#7bc96f' -%}
        {% else -%}
            {% set color = '#196127' -%}
        {% endif -%}
        squares{{ year }}.insertAdjacentHTML('beforeend', `<li class="dropdown-gh" data-toggle="tooltip-gh" title="{{ weight }} contribution(s) on {{ date_grid[year][i] }}" data-list="{{ grid_data[year][i] }}" style='background-color:{{ color }}'></li>`);
        {% endfor %}
    {% endfor %}
</script>

'''

tm = Template(html_code_template)
msg = tm.render(years=years, grid_data = construct_grid, date_grid = date_grid)

hugo_template_writer = '''
{{ define "header" }}
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/styles/atom-one-dark.min.css"
  />
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="{{ "/css/layouts/notes.css" | relURL}}">
  <link rel="stylesheet" href="{{ "/css/navigators/sidebar.css" | relURL}}">
  <link rel="stylesheet" href="{{ "/css/tcc_public/tcc_styles.css" | relURL}}">
{{ end }}

{{ define "navbar" }}
    {{ partial "navigators/navbar-2.html" . }}
{{ end }}

{{ define "sidebar" }}
  {{ $homePage:="#" }}
  {{ if site.IsMultiLingual }}
    {{ $homePage = (path.Join (cond ( eq .Language.Lang "en") "" .Language.Lang) .Type) }}
  {{ end }}

{{ end }}

{{ define "content" }}
<section class="content-section" id="content-section-gh"> ''' + msg + '''
</section>
{{ end }}

{{ define "scripts" }}
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.1/highlight.min.js"></script>
  <script>
    hljs.initHighlightingOnLoad();
  </script>
  {{ if .Params.math }}
      {{ partial "math.html" . }}
  {{ end }}
{{ end }}

'''

with open('themes/theme/layouts/gh-contrib/single.html', 'w') as f:
    f.write(hugo_template_writer)

# Copies contents of static theme to toha theme css directory
shutil.copyfile(f'{filepath}/tcc_public/tcc_styles.css', 
    'themes/theme/static/css/tcc_public/tcc_styles.css')