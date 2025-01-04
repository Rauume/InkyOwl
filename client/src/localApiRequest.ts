// import { API_ADDRESS, CLIENT_ADDRESS } from '$env/static/private';


export async function requestFromAPI(pathname: string) {
    // console.log("Fetching rand from aip")
    
    // const response = await fetch('/api/rand');
    // const data = await response.json();
    console.log("getting number")
    
    
    const url = new URL(pathname, "http://10.0.1.114:3000/").href
    const request = new Request(url);
    
    
    // console.log(request)
    const response = await fetch(request);
    const data = await response.json();
    
    console.log("Test Number: ", data)
    
    return fetch(request);
}