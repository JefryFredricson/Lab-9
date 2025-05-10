function addCity() {
    let cityName = document.getElementById('city_name').value
    let date_of_visit = document.getElementById('date_of_visit').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'city_name': cityName,
                             'date_of_visit': date_of_visit,
                             })
    })
}
function clean_list() {
    response = fetch('/delete', {
      method: 'DELETE',
    })

}