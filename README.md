Store
====
 * Description:A service to store crawler result
 * Build
   * docker-compose run web python ./manage.py makemigrations
   * docker-compose run web python ./manage.py migrate
   * docker-compose run web python ./manage.py createsuperuser
   * docker-compose up
 * API
   * path: /api/addPost/
   * Method: Post
   * Parameters:
     * title
     * author
     * date
     * label
     * content
