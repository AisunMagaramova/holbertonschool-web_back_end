// taskFirst funksiyasi yaradilir
export function taskFirst (){
	// const istifade edirik cunki sonradan deyeismeyecek
	const task = 'I prefer const when I can.';
	// task deyisen deyeri qaytarir
	return task;
}
export function getLast(){
	return 'is okay';
}

// taskNext adli funksiya yatrdilir
export function taskNext (){

	//combinationadli adli deyisen yaradilir
	//let istifade edirik cunki sonra deyeri deyisdireceyik
	let combination = 'But sometimes let';

	// combination deyisenini deyeri yeniden deyisdiririk 
	combination += getLast();

	return combination;
}
