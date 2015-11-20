from mixpanel import Mixpanel

mp = Mixpanel(d1bab48c9cc4ca3c8f5879bd455a74a7)

# Tracks an event, 'Sent Message',
# with distinct_id user_id
mp.track(user_id, 'Sent Message')

# You can also include properties to describe
# the circumstances of the event
mp.track(user_id, 'Plan Upgraded', {
    'Old Plan': 'Business',
    'New Plan': 'Premium'
})