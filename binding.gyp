{
  "targets": [
    {
      "target_name": "node-gd",
      "sources": ["cpp/node-gd.cpp"],
      "libraries": ["-lgd"],
      "conditions": [
        [ "OS=='freebsd'", {
          "libraries": ["-L/usr/local/lib"],
          "include_dirs": ["/usr/local/include"]
        }]
      ]
    }
  ]
}
