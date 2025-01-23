// import { API_ADDRESS, CLIENT_ADDRESS } from '$env/static/private';


export async function requestJsonFromAPI(pathname: string) {
    console.log("Requesting from API")
    
    const url = new URL(pathname, "http://10.0.1.114:3000/").href
    const request = new Request(url);
    const response = await fetch(request);
    //pre-convert to json to avoid confusion elsewhere
    const data = await response.json();
    return data;
}