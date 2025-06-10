function revealCell(row, col) {
    fetch(`/click/${row}/${col}`, { method: 'POST' })
        .then(() => location.reload());
}

function resetGame() {
    window.location.href = '/reset';
}
