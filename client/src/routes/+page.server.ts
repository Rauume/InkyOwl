

export async function load({ fetch }) {
	// const response = await fetch('/a');

	// return {
	// 	message: await response.text()
    // };
    console.log("Doing a test load");
    
    // const response = await fetch('/api/rand');
    // const response = await fetch('https://www.reddit.com/r/M43/comments/1hqrc8f/oh_why_not_16000_iso/.json')
    
    const response = await fetch('/api/rand');
    const data = await response.json();
    console.log("Your number is: ", data);
}
