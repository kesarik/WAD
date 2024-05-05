const {MongoClient}=require('mongodb') //import the mongoclient class,MongoClient is used to connect to a MongoDB server.
const url="mongodb://localhost:27017" //specifies the URL of the MongoDB server.
const database='student';
const client=new MongoClient(url);

const dbConnect=async()=>{
    const result=await client.connect(); //this line connect to mongo db server
    const db=await result.db(database); //gets a reference to the 'student' database using the db() method
    return db.collection('profile')
}
/*
async function dbConnect() {
    try {
        const client = new MongoClient(url, { useNewUrlParser: true, useUnifiedTopology: true });
        await client.connect();
        console.log("Connected to MongoDB");

        const db = client.db(database);
        return db.collection('profile');
    } catch (error) {
        console.error("Error connecting to MongoDB:", error);
        throw error; // Throw the error to handle it where this function is called
    }
}

*/
module.exports=dbConnect;

