<!DOCTYPE html>
<html>
<head>
    <title>User Management</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 40px;
            background: url('https://images.unsplash.com/photo-1519389950473-47ba0277781c') no-repeat center center fixed;
            background-size: cover;
            colour ="red"
            colour ="green"
            colour ="blue-dark"
        }

        h1, h2 {
            color: white;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.6);
        }

        form {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        input {
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            outline: none;
        }

        button {
            padding: 8px 15px;
            border: none;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
            border-radius: 4px;
        }

        button:hover {
            background-color: #45a049;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li {
            background: rgba(255, 255, 255, 0.85);
            padding: 10px;
            margin-bottom: 5px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <h1>Users</h1>

    <form id="userForm">
        <input type="text" id="name" placeholder="Name" required>
        <input type="email" id="email" placeholder="Email" required>
        <button type="submit">Add User</button>
    </form>

    <h2>User List</h2>
    <ul id="userList"></ul>

    <script>
        const API_URL = "http://54.158.5.91:5000/users"; // Public IP of backend

        function fetchUsers() {
            fetch(API_URL)
                .then(res => res.json())
                .then(data => {
                    const list = document.getElementById("userList");
                    list.innerHTML = "";
                    data.forEach(user => {
                        const li = document.createElement("li");
                        li.textContent = `${user.name} - ${user.email}`;
                        list.appendChild(li);
                    });
                });
        }

        skjfjkfhbfhfjfbhbfrgfbhfbrkjberkjbfjkbejkbbvdhbfdrgffbhjbffjhbfb tihsbfb jb thisis khald jamadar this is devops cloud devops enginneerr eei he 
            });
        });

        fetchUsers();
    </script>
</body>
</html>

