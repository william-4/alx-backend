import { createClient } from 'redis';

const client = createClient();

client.connect();

client.on('connect', function() {
		console.log('Redis client connected to the server');
})

client.on('error', (error) => {
		console.log(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
		client.set(schoolName, value);
}

function displaySchoolValue(schoolName) {
		client.get(schoolName, function(error, result) {
			if (error) {
				console.log(error);
				throw error;
			}
			console.log(result);
		});
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
