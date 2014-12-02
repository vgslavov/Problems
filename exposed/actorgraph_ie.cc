using namespace std;

// TODO: finish implementation (use hash_map?)
class ActorGraphNode {
	public:
		ActorGraphNode(string name);
		void linkCostar(ActorGraphNode costar);
		int getBaconNumber();
		void setBaconNumbers();
	private:
		string name;
		int baconNumber = -1;
		vector<ActorGraphNode> linkedActors;
};

ActorGraphNode::ActorGraphNode(string name)
{
	this.name = name;
}