import json
from absl import app
from absl import flags

flags.DEFINE_integer('number', 200, 'The member number for raffle')

FLAGS = flags.FLAGS


def generate_member():
    member = []
    for member_id in range(1, FLAGS.number + 1):
        member.append({
            "phone": "No.%s" % (member_id),
            "name": "No.%s" % (member_id)
        })
    return member

def main(argv):
    del argv
    member = generate_member()
    with open("member.js", mode='w') as m:
        print('var member = ', file = m, end='')
        print(json.dumps(member, indent = 2), file = m) 

if __name__ == '__main__':
    app.run(main)