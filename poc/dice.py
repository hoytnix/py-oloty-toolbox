from random import uniform
from time   import sleep
import hmac, hashlib

def roll(hash_server, hash_client):
  # Hash, hash, pl0x.
  hash_server = bytes(hash_server, 'utf-8')
  hash_client = bytes(hash_client, 'utf-8')
  _hmac = hmac.new(key=hash_server, msg=hash_client, digestmod=hashlib.sha256)
  _hash = _hmac.hexdigest()

  # Loop-d-loop, until less than 10^6
  i = 0
  lucky = int(x = _hash[i * 5: i * 5 + 5] , base = 16)
  while lucky >= 10**6:
    i += 1
    lucky = int(x = _hash[i * 5: i * 5 + 5] , base = 16)

    # Astronomically-impossible!
    if (i * 5 + 5) > 128:
      lucky = 99.99
      break

  # We need xx.xx!
  lucky %= 10**4 #0-999,999 -> 0-9,999
  lucky /= 10**2 #0-9,999   -> 0-99.99

  return (lucky, _hash)

def run(currency=100.0, payout=2.0, bet=1.0):
  # Crypto:
  hash_server = '76s0bq2hyvs912o71elihv4akc4l83m4hhla1lxfnuobh0s4bx2z7cxg8ewnjy0x'
  hash_client = 'pomddadjjl6pumlobwjqouizg36mwmtx'
  nonce       = 1

  # Calculate chances.
  chance = 100.0 / payout * 0.99

  # Infos.
  print("Payout: [%.2f] | Chance: [%.2f] | Currency: [%.2f]\n" % ( payout, chance, currency ) )

  # RUNNNNN!
  while currency > bet:

    # Remove cost.
    currency -= bet

    # Roll.
    lucky, _hash = roll(hash_server, '%s-%d' % (hash_client, nonce))

    # Win?
    win = lucky < chance
    if win:
      currency += bet * payout
    print("%.2f / %.2f | %.2f [%s] {%d}" % (lucky, chance, currency, _hash[:32], nonce))

    # Iterate.
    nonce += 1
    sleep(1)

def main():
  # Variables:
  currency = 100.0
  payout   = 7.5
  bet      = 1.0

  # Run.
  run(currency=currency, payout=payout, bet=bet)
  #run()

if __name__ == "__main__":
  main()
