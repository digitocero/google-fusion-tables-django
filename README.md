## README

### How to run:
    
    - run:
    
        python3 -m venv .ve
        source .ve/bin/activate
        pip install -r requirements.txt
        ./manage.py migrate
        ./manage.py runserver
    or
        make install
        make run
        
    - go to [google console](https://console.developers.google.com/)
    
        - generate a service account key with the right permissions
        Place it next to this README.md as `service_account_key.json`
        If we want another name we can change it in settings.SERVICE_ACCOUNT_KEY
        
        - generate also a api key for the map. Copy the value in
        settings.GOOGLE_API_KEY
    
    - in fusion tables create a table with columns lat, lon, address
        copy the (encrypted) name of the table in settings.FUSION_TABLE_NAME

    There is a standard django /admin/ page to explore the local data
    To access it, go to localhost:8000/admin/
        user: admin
        pass: adminadmin
    or recreate the superuser running:
        make createsuperuser


### Implementation details:

    - We tried to keep it as simple as possible
    - the single page app includes a csrf token to avoid cross site requests
    -We used this documentation
        https://developers.google.com/fusiontables/docs/v2/reference/query
        https://developers.google.com/identity/protocols/googlescopes#fusiontablesv2
        https://developers.google.com/maps/documentation/javascript/fusiontableslayer
        https://developers.google.com/fusiontables/docs/v2/reference/query/sql
        https://github.com/google/google-api-python-client/blob/master/samples/django_sample/plus/views.py

    - A Makefile is included to run some commands easier
        (in the shell makefiles get autocomplete too)


### Assumptions:

    - We dont have a preference for a mapping company.
        google maps is used

    - Deployment and serving from a real server is not considered:
        The app runs on the local python server
        No nginx/apache configuration is included


### Ideas for improvements:
    - js, css should be on its own file
        Did not already do this because
        then we would need ./manage.py collectstatic
    - jquery could have a local version in addition to the cdn
        We could also get rid of jquery or replace for some framework.
    - return proper json in API
    - Validate addresses using other third-parties (ups)
        google reverse geocode is not very accurate if we are near the coast, for instance.
    - Add a date in the Location model to record when a Location was added
        to get analytics and usage patterns
    - The async js can start soon having too many indentations.
        We could refactor it with promises or a similar method to flatten it.
    -if the REST api grows: django rest framework
        json-schema
    - Store Models as spatial data for more advanced processing

