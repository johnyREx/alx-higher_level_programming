#!/usr/bin/node
const numArgs = process.argv.lenght - 2;
if (numArgs === 0)
{
	console.log('No Argument');
}
else if (numArgs === 1)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
