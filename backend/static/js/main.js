const deletePerson = (id) => {
    fetch(`/person/${id}`, {method: 'DELETE'})
    .then(resp => {
        window.location.reload();
    });
};