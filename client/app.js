const SERVER_URL = 'http://127.0.0.1:5000'

function handleLogin (response) {
    localStorage.setItem("token", response.credential);
}

function onLinkAdsAccount() {
    token = localStorage.getItem("token");
    window.location.href = `${SERVER_URL}/authentication?token=${token}`
}