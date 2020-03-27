
ABSTRACT
--------

__Problem Statement:__ 
The idea is to develop a parser that reads etc/passwd and etc/group and generate a user json containing user id, user full name and groups the user belong

__Language Used:__
Python3 is used for the development 

__Process:__
The idea to is to collect the data from each file and use a dictionary, pojo class to store the data. The data then is collected from group file to add it to the groups of the user. During development, different type of exceptions are considered and are implemented in the working code.

__Output:__

```json
{
	"list": {
		"uid": "38",
		"full_name": "Mailing List Manager",
		"groups": []
	},
	"nobody": {
		"uid": "65534",
		"full_name": "nobody",
		"groups": []
	},
	"lxd": {
		"uid": "106",
		"full_name": "",
		"groups": []
	},
	"ubuntu": {
		"uid": "1000",
		"full_name": "Ubuntu",
		"groups": [
			"adm",
			"cdrom",
			"dip",
			"docker",
			"netdev",
			"plugdev",
			"floppy",
			"dialout",
			"audio",
			"lxd",
			"sudo",
			"video"
		]
	},
	"man": {
		"uid": "6",
		"full_name": "man",
		"groups": []
	}
}
```

