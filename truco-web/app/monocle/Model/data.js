var CONFIG = {
    name: 'truco_db',         //Name of the database
    version: '0.1',           //Version of the database
    schema: [                 //Database schema
        {
            name: 'list',     //Table name
            drop: false,       //Drop existing content on init
            fields: {         //Table fields
              id: 'INTEGER PRIMARY KEY',
              name: 'TEXT',
              description: 'TEXT',
              type: 'STRING',
              completed: 'INTEGER DEFAULT 0',
              created_at: 'DATETIME',
              modified_at: 'DATETIME'
            }
        },
        {
            name: 'list_item',
            fields:{
                id: 'INTEGER PRIMARY KEY',
                list: 'INTEGER NOT NULL',
                product: 'INTEGER NOT NULL',
                quantity : 'INTEGER DEFAULT 0',
                dirty : 'INTEGER DEFAULT 0'
            }
        },
        {
            name: 'product',
            fields:{
                id: 'INTEGER PRIMARY KEY',
                name: 'TEXT',
                category: 'INTEGER',
                description: 'TEXT',
                created_at: 'DATETIME',
                modified_at: 'DATETIME'
            }
        },
        {
            name: 'category',
            fields:{
                id: 'INTEGER PRIMARY KEY',
                name: 'TEXT',
                description: 'TEXT'
            }
        }
    ]
};
Lungo.Data.Sql.init(CONFIG);