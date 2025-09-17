# Namer

Generate names in the form of adjective noun with the same starting letter

Done in an imaginative way to overdo a simple task

## Initialize

* install docker
* git pull this repo
* docker build -t namer:$(date +%Y%m%d) .
* docker run -d -p 9977:5000 --name namer namer:$(date +%Y%m%d)
* open browser and navigate to http://localhost:9977

## Authors

* **Adam Mohr** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
